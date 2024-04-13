minikube/start:
	minikube start

minikube/delete:
	minikube delete

minikube/dashboard:
	minikube dashboard

kubectl/deploy/all:
	cd kube-configs && kubectl apply -f '*.yaml'

kubectl/delete/all:
	cd kube-configs && kubectl delete -f '*.yaml'

kubectl/delete/services:
	kubectl delete -n default deployment api mysql

kubectl/deploy/services:
	cd kube-configs && kubectl apply -f api-deployment.yaml,mysql-deployment.yaml

kubectl/pods:
	kubectl get pods -A

run:
	minikube service api