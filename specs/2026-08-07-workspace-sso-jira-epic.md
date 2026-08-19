# Jira epic draft: Workspace SSO (SAML 2.0)

Ready to paste. Fields per the usual epic layout; adjust project/labels to taste.

---

**Type:** Epic
**Summary:** Workspace SSO (SAML 2.0) - enterprise identity federation
**Labels:** enterprise, security, identity
**Priority:** High

## Why now

- Gartner No-Code Agent Builder submission, requirement 2 ("Integrate with enterprise identity
  and access management systems to enable secure agent deployment") is the only unevidenced
  requirement and blocks the submission. Every requirement needs a supporting docs URL; a crawl
  of all live docs pages (2026-08-07) returned zero matches for SSO/SAML/LDAP/SCIM.
- The pricing page already sells SSO/SAML at Business and LDAP at Enterprise, and the FAQ names
  Okta, Azure AD, Google Workspace, and OneLogin. We currently sell a capability that does not
  exist.
- Enterprise security reviews ask for the SSO docs page by name; its absence is conspicuous next
  to Compliance & Security.

## Product framework (decided in design review, 2026-08-07 - see design doc)

Three layers, one owner each: **identity** (the customer's IdP - who you are), **membership**
(the Team roster, by invitation - you belong), **reach** (Permissions - what you can touch).
SSO is a **workspace authentication policy**: the IdP decides who gets in the door, FlowRunner
decides who belongs and what they can reach. The Team page's model and "no per-seat charges"
are untouched.

Decisions: per-workspace SSO (no org layer, no domain claiming); invitation-only membership (no
JIT admission); members of an enforced workspace never need a FlowRunner password; SAML 2.0 only
in v1 ("any SAML 2.0 IdP" is the support statement).

## Requirements

### Admin configuration
1. Workspace Settings gains a "Single Sign-On" section, Business plan and up; below Business it
   shows the upgrade path.
2. The section displays FlowRunner's SP details (ACS URL, Entity ID, metadata URL) with copy
   buttons.
3. The admin configures the IdP by pasting a metadata URL or uploading metadata XML (auto-fills
   SSO URL, issuer, signing certificate); manual fields as fallback.
4. Matching rule stated in the UI: assertion NameID = email, matched against invited roster
   members.
5. "Test connection" runs a live assertion in a popup with the admin's own IdP account and shows
   the parsed result.
6. States: Not configured -> Configured (optional) -> Enforced. Enforced is unreachable without
   a passing test connection.

### Enforcement
7. "Require SSO for this workspace": on, every member entering needs a fresh IdP assertion, and
   password entry to this workspace stops working.
8. Break-glass: the workspace Owner always retains FlowRunner-credential access; stated in the
   UI next to the toggle.

### Member sign-in
9. Invite acceptance for an SSO workspace goes straight to the IdP; the account is created or
   linked on the first assertion, with no password step.
10. Login page gains a "Sign in with SSO" path (email in, redirect out).
11. IdP-initiated sign-in works (IdP dashboard tile lands the member in the workspace).
12. A member may hold a password for other workspaces; the enforced workspace always demands the
    IdP.

### Deprovisioning
13. When the IdP stops asserting a member, their next entry attempt shows a lockout screen
    naming the workspace and pointing at their admin. The roster row remains until the admin
    removes it. Flows are workspace-scoped and keep running (confirm - open question 6).

### One account, many credentials
14. An account holds multiple sign-in methods: optional password plus durable IdP links (bound
    at first assertion; account-email changes do not break the binding). No re-registration in
    any scenario.
15. A password-less user creating a workspace (becoming its Owner) is prompted to set a password
    (email-verified) as part of the flow - coheres with requirement 8.
16. A password-less user accepting a non-SSO invite gets the same prompt, skippable, with a
    warning that the access otherwise rides on the employer's IdP. "Set a password" is always
    available in account settings.

## Non-goals (v1)

OIDC (fast-follow), SCIM/automated provisioning, JIT admission, LDAP (separate effort; stays on
the roadmap for Enterprise), an Organization layer above workspaces, consolidated billing,
per-workspace session policies.

## Open questions (product/engineering to answer)

1. Session lifetime of a workspace assertion; re-auth cadence.
2. Enforcement toggle / deprovisioning: kill active sessions, or bite at next entry?
3. Assertion signing/encryption requirements.
4. One IdP serving several workspaces without duplicate configuration.
5. Audit logging: SSO config changes, break-glass sign-ins.
6. Confirm flows have no personally-owned runtime dependency (deprovisioning assumption).

## Acceptance criteria

- A Business-plan workspace admin configures Okta via metadata URL, passes test connection,
  enforces SSO, and a password-less invited member enters via both SP-initiated and
  IdP-initiated sign-in.
- With enforcement on, password entry to the workspace fails for members and succeeds for the
  Owner.
- Enforcement cannot be enabled without a passing test connection.
- A member removed at the IdP is locked out at next entry with the designed screen; the roster
  row and workspace flows are unaffected.
- A password-less member creates their own workspace and ends the flow holding a working
  password credential.
- Below-Business workspaces see the gated section with the upgrade path.

## Follow-ups (not this epic)

- Docs: `platform/single-sign-on.md` written against the shipped product (existing brief on
  file), plus named IdP setup guides (Okta, Entra ID, Google Workspace, OneLogin).
- OIDC support; LDAP scoping exercise; SCIM evaluation once enterprise demand shows.
