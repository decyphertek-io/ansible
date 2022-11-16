amazon.aws.ec2_instance module:
================================

Supported parameters include:
----------------------------- 

    wait, validate_certs, tags (resource_tags), access_key (aws_access_key, aws_access_key_id, ec2_access_key), security_group, profile (aws_profile), endpoint_url (aws_endpoint_url, ec2_url, s3_url), instance_type, vpc_subnet_id (subnet_id), aws_config, placement_group, network, wait_timeout, image, image_id, name, instance_initiated_shutdown_behavior, launch_template, termination_protection, detailed_monitoring, purge_tags, aws_ca_bundle, debug_botocore_endpoint_logs, count, exact_count, ebs_optimized, session_token (access_token, aws_security_token, aws_session_token, security_token), availability_zone, secret_key (aws_secret_access_key, aws_secret_key, ec2_secret_key), cpu_credit_specification, state, hibernation_options, security_groups, aap_callback (tower_callback), user_data, key_name, region (aws_region, ec2_region), filters, cpu_options, instance_ids, iam_instance_profile (instance_role),

AWS CLI
-------

    $ aws ec2 describe-instances
    $ ec2 start-instances --instance-ids i-0000000000000
    $ ec2 stop-instances --instance-ids i-0000000000000

    
