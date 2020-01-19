"""
Name: job_initiator.py
Description: 動的に manifest を作成し, job を実行する
Created by: Masato Shima
Created on: 2020/01/19
"""

# **************************************************
# ----- Import Library
# **************************************************
import os

import pika
from kubernetes import client, config


# **************************************************
# ----- Constants & Variables
# **************************************************
OBJECT_NAME = "pngen"
QUEUE_NAME = "task-queue"


# **************************************************
# ----- Function main
# **************************************************
def main():
	# kubernetes の job に渡す parameter
	job_params = [
		[1, 1000],
		[1001, 2000],
		[2001, 3000],
		[3001, 4000]
	]

	# job の実行数
	completions = len(job_params)

	# job の並列実行数
	parallelism = 2

	# RabbitMQ へ接続
	queue = create_queue()

	# RabbitMQ へ message を送信
	for job_param in job_params:
		queue.basic_publish(
			exchange="",
			routing_key=QUEUE_NAME,
			body=f"{job_param[0]},{job_param[1]}"
		)

	# .kube の読み込み
	config.load_kube_config()

	# job を生成し, それらを実行
	client.BatchV1Api().create_namespaced_job(
		body=create_job_manifest(completions, parallelism),
		namespace="default"
	)

	return


# **************************************************
# ----- Function create_queue
# **************************************************
def create_queue() -> pika.BlockingConnection.channel:
	# RabbitMQ へ接続
	queue_cred = pika.PlainCredentials("guest", "guest")
	queue_host = "192.168.99.100"
	queue_port = 31672

	queue_param = pika.ConnectionParameters(
		host=queue_host,
		port=queue_port,
		credentials=queue_cred
	)

	connect = pika.BlockingConnection(queue_param)
	channel = connect.channel()
	channel.queue_declare(queue=QUEUE_NAME)

	return channel


# **************************************************
# ----- Function create_job_manifest
# **************************************************
def create_job_manifest(n_comp, n_para):
	# 引数で渡された情報にもとづき, Kubernetes の job を生成する
	container = client.V1Container(
		name="job-worker",
		image="masato0921/tutorial-docker-kubernetes:chapter_010_006",
		env=[
			client.V1EnvVar(
				name="BROKER_URL", value="amqp://guest:guest@task-queue:5672"
			),
			client.V1EnvVar(
				name="QUEUE", value="task-queue"
			)
		]
	)

	template = client.V1PodTemplateSpec(
		spec=client.V1PodSpec(
			containers=[container],
			restart_policy="Never"
		)
	)

	spec = client.V1JobSpec(
		backoff_limit=4,
		template=template,
		completions=n_comp,
		parallelism=n_para
	)

	job = client.V1Job(
		api_version="batch/v1",
		kind="Job",
		metadata=client.V1ObjectMeta(name=OBJECT_NAME),
		spec=spec
	)

	return job


# **************************************************
# ----- Main
# **************************************************
if __name__ == '__main__':
	os.chdir(os.path.dirname(os.path.abspath(__file__)))

	main()


# **************************************************
# ----- End
# **************************************************
