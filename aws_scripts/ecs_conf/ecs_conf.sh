#Configuring ecs-cli
ecs-cli configure profile --profile-name ecspoc --access-key 'AKIAXJIV5XUGFVFNAD4Z' --secret-key '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'

# ecs up using default aws profile
ecs-cli compose --file jenkins/tmp/docker-compose.yml --ecs-params jenkins/tmp/ecs-params.yml up --aws-profile default

# ecs up with dev-admin profile
ecs-cli compose --file jenkins/tmp/docker-compose.yml --ecs-params jenkins/tmp/ecs-params.yml up --aws-profile dev-admin