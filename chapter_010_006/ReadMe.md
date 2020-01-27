# job_initiator の container を実行する際は, 以下のコマンドで実行すること

``` console

docker run -it --rm --name kube \
  -v `pwd`/chapter_010_006/job_initiator:/py \
  -v ~/.kube:/root/.kube \
  -v ~/.minikube:/home/ubuntu/.minikube \
  masato0921/tutorial-docker-kubernetes:job_init \
  bash

```

End
