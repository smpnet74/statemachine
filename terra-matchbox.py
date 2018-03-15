import subprocess

def lambda_handler(event,context):
  args = "./terraform plan --var-file prod.tfvars --var-file secret.tfvars"
  result = subprocess.check_output(args, shell=True)
  return result
