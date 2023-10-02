# store hello=world in Parameter Store

resource "aws_ssm_parameter" "hello" {
  name  = "/hello-1122"
  type  = "String"
  value = "world"
}
