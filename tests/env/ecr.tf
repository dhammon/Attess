
resource "aws_ecr_repository" "private_repo" {
  name                 = "private_repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }
}

resource "aws_ecr_repository" "public_repo" {
  name                 = "public_repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }
}

resource "aws_ecr_repository_policy" "public_policy" {
  repository = aws_ecr_repository.public_repo.name

  policy = <<EOF
{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "public policy",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "ecr:*"
            ]
        }
    ]
}
EOF
}

