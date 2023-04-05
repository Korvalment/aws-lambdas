StartNewProject is the main fuction

This lambda will:
 1) Create new Cognito User Pool with 2 clients:
       1a) Create User Pool
       1b) Create SSO integration
       1c) Create SSO integration example
  2) Create new IAM policy for that Cognito Pool to integrate (SAML) SSO (integration management)
  3) Create user in (!!!)Amplify User Pool(!!!)
  4) Attach policy to user
  5) Save: user_id, coognito_pool_id, clients_id to DynamoDB

This will be implemented by:
  function CreateUserPool(user_pool_name) that returns [user_pool_id, user_pool_arn]
  function CreateClient(user_pool_id) that will return client_id
  function CreatePolicy(user_pool_arn, policy_name) that returns policy_arn
  function CreteUser(amplify_pool_id, user_mail) that returns user_id
  function AttachPolicy(user_id, policy_arn)
  [user_pool_id, cient1_id, client2_id, user_id] >> DynamoDB
