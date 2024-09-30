# Load balancer configuration

### 1. Create targets
You should create 2 target groups for port 80 and port 443
Go through the following steps for each target group

1. Go to `EC2 > Target groups` and press `Create target group` button
2. Choose `Instances` as target type
3. Provide `Target group name`:
   - bl-ingress-80
   - bl-ingress-443
4. Choose `TCP` protocol and the following ports for each target group:
    ```
    80 - bl-ingress-80
    443 - bl-ingress-443
    ```
5. Select the same VPC as for you EC2 instance
6. Use `TCP` health check
7. Press `Next` button 
8. Choose instance with backendless pro
9. Press `Include as pending bellow` button
10. Press `Create target group`button

At the end your target page should look like the on the following screen
![](img/target-groups-for-nlb.png)

### 2. Create Load balancers
You should create Network Load Balancer.
Go through the following steps for each load balancer

1. Go to `EC2 > Load balancers` and press `Create load balancer` button
2. Use `Network Load Balancer` type
3. Provide `Load balancer name`
   - bl-ingress
4. Use `Internet-facing` as schema 
5. Use `IPv4`
6. Choose `Network mapping` and `Security groups`
7. For `Listeners and routing` and routing use `TCP` protocol:
   ![](img/listeners-and-routing-for-nlb.png)
8. Press `Create load balancer` button

At the end your Load balancers page should look like the on the following screen
![](img/nlb-view.png)

### 3. Create domains 
1. Go to `Route 53 > Hosted zones > your-domain.com`
2. Press `Create record` button
3. You should create 3 subdomain
   - bl-api
   - bl-console
   - bl-rt
4. Choose `CNAME` as record type
5. Provide load balancer `DNS name` as Value
    ![](img/route53-create-record.png)
6. Press `Create records` button
![](img/route53-page.png)

### 4. Configure domain in Pro Manager
{% include-markdown "../../configuration/domain-configuration-include.md" %}