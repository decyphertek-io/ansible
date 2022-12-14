###Azure AD MFA ### 
#from oauthenticator.azuread import AzureAdOAuthenticator 
#c.JupyterHub.authenticator_class = AzureAdOAuthenticator 
#c.Application.log_level = 'DEBUG' 
#c.AzureAdOAuthenticator.tenant_id = 'AAD_TENANT_ID'
#c.AzureAdOAuthenticator.oauth_callback_url = 'https://domain_or_ip/hub/oauth_callback' 
#c.AzureAdOAuthenticator.client_id = 'AAD_APP_CLIENT_ID'
#c.AzureAdOAuthenticator.client_secret = 'AAD_APP_CLIENT_SECRET'
#c.AzureAdOAuthenticator.scope = ['openid','profile']
#c.AzureAdOAuthenticator.username_claim = ‘upn' OR 'given_name’

###Server Config### 
#0.0.0.0 if using PAM, if using AzureAD , need to set server IP. Can set any port, avoid port conflicts.
c.JupyterHub.ssl_key = '/etc/ssl/private/private-ssl.key' 
c.JupyterHub.ssl_cert = '/etc/ssl/certs/private-ssl.crt'
c.JupyterHub.ip = '0.0.0.0' 
c.JupyterHub.port = 443

###Admin Spawner### 
c.JupyterHub.admin_access = True 

###Notebook Idle Shutdown### 
c.ServerApp.shutdown_no_activity_timeout = 60 * 60
c.MappingKernelManager.cull_idle_timeout = 20 * 60
c.MappingKernelManager.cull_interval = 2 * 60

###Custom Logo###
#c.JupyterHub.logo_file = '/usr/local/share/jupyterhub/static/images/logo.png'

###Allowed Multiple named Servers###
c.JupyterHub.allow_named_servers = True
c.JupyterHub.named_server_limit_per_user = 5
