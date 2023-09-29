# store hello=world in Parameter Store

resource "aws_ssm_parameter" "hello" {
  name  = "/hello"
  type  = "String"
  value = "world"
}
