# NOTES

## Deploy with Kubernetes Deployment (Color App)

Manually create a Deployment pointing to an Image, then expose its Service for use.

    k create deploy color-app --image=mmumshad/simple-webapp-color --port=8080
    k expose deploy/color-app

FIXME: type=LoadBalancer

### Check

    watch curl -s localhost:8080

## Deploy with Helm Chart (Apache)

Deploy using a Helm Chart directly, with a config to correctly expose the Service for use.

FIXME: show HelmChart with working options

k expose deployment apache -nweb $DRY >apache-service.yaml
FIXME: type=LoadBalancer
FIXME: edit ports

### Check

Raw HTTP port works

    curl localhost:8081
    <html><body><h1>It works!</h1></body></html>

Ignore certificate on the https secure port

    curl -k https://localhost:8443
    <html><body><h1>It works!</h1></body></html>

Automatically exposes metrics!

    curl -s localhost:9117/metrics | grep -E code=.200
    promhttp_metric_handler_requests_total{code="200"} 278

## create and start Kubernetes (K3s) cluster

NOTE: need 4G ram

    colima start --cpu 2 --memory 4 --with-kubernetes
