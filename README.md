StartNewProject is the main fuction

This lambda will:
 1) Create new Cognito User Pool with 2 clients:
  a) Create User Pool
  b) Create SSO integration
  c) Create SSO integration example
 2) Create new IAM policy for that Cognito Pool to integrate (SAML) SSO (integration management)
 3) Create user in (!!!)Amplify User Pool(!!!)
 4) Attach policy to user
 5) Save: user_id, coognito_pool_id, clients_id to DynamoDB
