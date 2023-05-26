## Install MetalLB on minikube

```
kubectl apply -f https://raw.githubusercontent.com/google/metallb/v0.8.3/manifests/metallb.yaml
```

## Apply the config

Make sure the addresses contain $(minikube ip):

```
kubectl apply -f metal-lb-config.yaml
```
