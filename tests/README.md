# Setup Test Environment
```
aws conifgure
    #enter test account credentials
cd attess/tests/env/
terraform init
terraform apply
```


# Configure Data
1. Rename tests/config.py.example to tests/config.py
2. Update variable information


# Run Tests
- `python3 -m unittest discover tests/`
- `python3 -m debugpy --listen 5678 --wait-for-client tests/test_accounts.py TestAccounts.test_displayMessage` -> then Run Debug Attach
- `alias debug="python3 -m debugpy --listen 5678 --wait-for-client"`