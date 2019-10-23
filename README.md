# rundeck-ansible

This is a project to deploy Rundeck via ansible.

It contains the following components:
- rundeck
- rundeck cli
- postgres (for project storage)
- AWS Node Source
- Nginx to proxy rundeck (TODO: SSL termination on NGINX)
- Basic python script to turn instances on and off using boto3

This only supports CentOS7/RHEL7.

All variables in group_vars/all/main.yml
