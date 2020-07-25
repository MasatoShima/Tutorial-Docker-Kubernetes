# MFA トークンの取得〜スイッチロールによる AWS CLI 経由でのリソースへのアクセスについて
1. MFA トークンの取得
``` bash
aws sts get-session-token --serial-number arn:aws:iam::ACCOUNTID:mfa/*****Developer-******** --token-code TOKENCODE
```
- 応答データの aws_access_key_id, aws_secret_access_key, aws_session_token は credentials ファイルに登録

2. スイッチロールに関する設定
```
[profile ********]
role_arn = arn:aws:iam::ACCOUNTID:role/ROLENAME
source_profile = default
```
- config ファイルにスイッチ先の IAM Role Arn を記載
- 以後, AWS CLI コマンド実行時に「--profile ********」を付与することで, スイッチロールした後にリソースへのアクセスが可能になる

## 参考
- [AWS CLI 経由で MFA を使用してアクセスを認証する](https://aws.amazon.com/jp/premiumsupport/knowledge-center/authenticate-mfa-cli/)
- [IAM ロールへの切り替え (AWS CLI) - AWS Identity and Access Management](https://docs.aws.amazon.com/ja_jp/IAM/latest/UserGuide/id_roles_use_switch-role-cli.html)

# kubeconfig に AWS EKS Cluster への認証情報を登録
``` bash
aws eks --region ap-northeast-1 update-kubeconfig --name CLUSTER NAME --role-arn arn:aws:iam::ACCOUNTID:role/ROLENAME
```
- ROLENAME は「2. スイッチロールに関する設定」と同一で可

End