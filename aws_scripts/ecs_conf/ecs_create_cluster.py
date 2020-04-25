import boto3


ecs_cli = boto3.client('ecs')
ecs_res = boto3.resource('ecs')

# Create ECS Cluster
def create_cluster(cluster_name):
    try:
      response = ecs_cli.create_cluster(
        clusterName=cluster_name
      )
      print(response)
    except BaseException as e:
        print(e)
