Julien GALERNE
Gor GRIGORYAN

This is a project that constitutes a simple example of a kubernetes cluster. To not create different repositories for each build, the branches correspond to different docker images with their own github actions workflow file.

To test the project, run

```bash
git checkout kubernetes
minikube start
kubectl apply -f nginx-app-deployment.yaml
kubectl apply -f pg-deployment.yaml
kubectl apply -f flask-app-deployment.yaml
```

This will deply 5 docker pods. Two pods that are nginx reverse proxies, two pods that are flask api apps and a postgres images.

Run

```bash
minikube ip
```

Enter the `http://{minikube ip}:30001` (usually it gives `http://192.168.49.2:30001/`)

Each time someone accesses this page a log is registered in the database. To see the logs go to `http://{minikube ip}:30001/logs` (`http://192.168.49.2:30001/logs`)

OR, if you are under Windows, Run
```bash
minikube service nginx-app-service
```

It will open your browser automatically on the right page. Same thing to access to logs.
