### Developer Registration Toggle

Controls whether developer registration is enabled.

| Configuration Property Path              | Type    | Default Value | Example                                    |
|------------------------------------------|---------|---------------|--------------------------------------------|
| `config/developerregistration/enabled`   | Boolean | `true`        | `config/developerregistration/enabled = false` |

### Email Confirmation Requirement

Determines if email confirmation is required for developer registration.

| Configuration Property Path                             | Type    | Default Value | Example                                                    |
|---------------------------------------------------------|---------|---------------|------------------------------------------------------------|
| `config/developerregistration/emailConfirmationRequired` | Boolean | `false`       | `config/developerregistration/emailConfirmationRequired = true` |

### Blocked Email Patterns

Defines a semi-colon-separated list of email patterns that are blocked for registration. Emails matching any pattern in the list will be blocked.

| Configuration Property Path                               | Type    | Default Value        | Example                                             |
|-----------------------------------------------------------|---------|----------------------|-----------------------------------------------------|
| `config/developerregistration/blockedEmailPatternsList`   | String  | `qq.com;rhyta.com`   | `config/developerregistration/blockedEmailPatternsList = example.com;test.com` |

### Google reCAPTCHA Settings

Enables or disables Google reCAPTCHA for the developer registration process.

| Configuration Property Path                               | Type    | Default Value | Example                                             |
|-----------------------------------------------------------|---------|---------------|-----------------------------------------------------|
| `config/developerregistration/captcha/enabled`            | Boolean | `false`       | `config/developerregistration/captcha/enabled = true` |

Specifies the client key for Google reCAPTCHA. Replace the placeholder with the actual client key obtained from Google.

| Configuration Property Path                               | Type    | Default Value | Example                                             |
|-----------------------------------------------------------|---------|---------------|-----------------------------------------------------|
| `config/developerregistration/captcha/clientKey`          | String  | N/A           | `config/developerregistration/captcha/clientKey = [your-client-key-here]` |

Specifies the server key for Google reCAPTCHA. Replace the placeholder with the actual server key obtained from Google.

| Configuration Property Path                               | Type    | Default Value | Example                                             |
|-----------------------------------------------------------|---------|---------------|-----------------------------------------------------|
| `config/developerregistration/captcha/serverKey`          | String  | N/A           | `config/developerregistration/captcha/serverKey = [your-server-key-here]` |