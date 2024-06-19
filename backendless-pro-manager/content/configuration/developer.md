# Developer configuration

### Developer Registration Toggle

- **`config/developerregistration/enabled`**
    - **Description:** Controls whether developer registration is enabled.
    - **Type:** Boolean
    - **Default:** `true`
    - **Example:** `config/developerregistration/enabled = false`

### Email Confirmation Requirement

- **`config/developerregistration/emailConfirmationRequired`**
    - **Description:** Determines if email confirmation is required for developer registration.
    - **Type:** Boolean
    - **Default:** `false`
    - **Example:** `config/developerregistration/emailConfirmationRequired = true`


### Blocked Email Patterns

- **`config/developerregistration/blockedEmailPatternsList`**
    - **Description:** Defines a semi-colon-separated list of email patterns that are blocked for registration. Emails matching any pattern in the list will be blocked.
    - **Type:** String
    - **Default:** `qq.com;rhyta.com`
    - **Example:** `config/developerregistration/blockedEmailPatternsList = example.com;test.com`

    
### Google reCAPTCHA Settings

- **`config/developerregistration/captcha/enabled`**
    - **Description:** Enables or disables Google reCAPTCHA for the developer registration process.
    - **Type:** Boolean
    - **Default:** `false`
    - **Example:** `config/developerregistration/captcha/enabled = true`

- **`config/developerregistration/captcha/clientKey`**
    - **Description:** Specifies the client key for Google reCAPTCHA. Replace the placeholder with the actual client key obtained from Google.
    - **Type:** String
    - **Example:** `config/developerregistration/captcha/clientKey = [your-client-key-here]`

- **`config/developerregistration/captcha/serverKey`**
    - **Description:** Specifies the server key for Google reCAPTCHA. Replace the placeholder with the actual server key obtained from Google.
    - **Type:** String
    - **Example:** `config/developerregistration/captcha/serverKey = [your-server-key-here]`



