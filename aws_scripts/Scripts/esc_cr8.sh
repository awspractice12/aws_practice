#Steps to be followed and taken form aws docs

# ECS_CLI_installation
# https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html

# get the install
sudo curl -o /usr/local/bin/ecs-cli https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-linux-amd64-latest

# Verify Using the MD5 Sum
echo "$(curl -s https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-linux-amd64-latest.md5) /usr/local/bin/ecs-cli" | md5sum -c -

# Verify Using the PGP Signature
gpg --keyserver hkp://keys.gnupg.net --recv BCE9D9A42D51784F

# Download the Amazon ECS CLI signatures.
curl -o ecs-cli.asc https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-linux-amd64-latest.asc

# Verify the signature.
sudo gpg --verify ecs-cli.asc /usr/local/bin/ecs-cli

#  Apply Execute Permissions to the Binary
sudo chmod +x /usr/local/bin/ecs-cli

# Complete the Installation
ecs-cli --version