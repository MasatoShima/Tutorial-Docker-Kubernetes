# """
# Name: request.sh
# Description: sample manifest from chapter 9.6
# Created by: Masato Shima
# Created on: 2020/01/05
# """

for pod in $(kubectl get pods | awk 'NR>1 {print $1}' | grep web-deploy); \
  do kubectl exec "$pod" -- /bin/sh -c "hostname > /usr/share/nginx/html/index.html"; \
done

# End
