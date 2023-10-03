
resource "aws_lambda_function" "lambda_hello" {
  function_name = "hello"
  handler = "lambda_hello.lambda_handler"
  runtime = "python3.8"
  
  filename      = "lambda_hello.zip"
  source_code_hash = filebase64sha256("lambda_hello.zip")
  
  role = aws_iam_role.lambda_role.arn
  
  timeout = 10
  memory_size = 128
}

# IAM Role for Lambda function
resource "aws_iam_role" "lambda_role" {
  name = "lambda_execution_role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# FIXME: Attach necessary permissions to the Lambda role, for example, to access S3
resource "aws_iam_policy_attachment" "lambda_policy_attachment" {
  name = "lambda_policy_attachment"
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess" # FIXME: Adjust the policy as needed
  roles      = [aws_iam_role.lambda_role.name]
}
