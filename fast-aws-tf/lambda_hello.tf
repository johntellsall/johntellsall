
resource "aws_lambda_function" "example_lambda" {
  function_name = "example_lambda_function"
  handler = "lambda_handler.lambda_handler" # This should match the handler function in your Python code
  runtime = "python3.8"
  
  # You can specify the execution role here or create it separately
  # role = aws_iam_role.lambda_role.arn
  
  # Zip your Python code and any dependencies into a deployment package
  filename      = "lambda_function.zip"
  source_code_hash = filebase64sha256("lambda_function.zip")
  
  # IAM Role for the Lambda function
  role = aws_iam_role.lambda_role.arn
  
  # Set the timeout and memory size for your Lambda function
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

# Attach necessary permissions to the Lambda role, for example, to access S3
resource "aws_iam_policy_attachment" "lambda_s3_attachment" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess" # Adjust the policy as needed
  roles      = [aws_iam_role.lambda_role.name]
}
