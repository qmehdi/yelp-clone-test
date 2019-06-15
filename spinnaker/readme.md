kubectl -n kube-system create sa tiller

kubectl create deployment hal --image gcr.io/spinnaker-marketplace/halyard:1.5.0

hal config security ui edit --override-base-url http://a022661133f8e11e9ad28028e0d3bbeb-1964368430.us-west-2.elb.amazonaws.com:9000 
hal config security api edit --override-base-url http://a01e9dd283f8e11e9ad28028e0d3bbeb-875074532.us-west-2.elb.amazonaws.com:8084

