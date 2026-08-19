# Workspace SSO (SAML 2.0) - product design

**Date:** 2026-08-07
**Status:** Approved by Mark (product owner) in design review, 2026-08-07
**Deliverable:** Jira epic for the product team (companion file:
`2026-08-07-workspace-sso-jira-epic.md`). Docs work follows the feature, not the other way
around - see "Origin" below.

## Origin
A marketing brief (`doc-brief-sso-enterprise-identity.md`) requested an SSO documentation page to
evidence Gartner No-Code Agent Builder requirement 2 ("Integrate with enterprise identity and
access management systems"). Product-owner review established the feature does not exist. The
demand signals are real: the pricing page already sells SSO/SAML at Business and LDAP at
Enterprise, the FAQ names Okta, Azure AD, Google Workspace, and OneLogin, and enterprise security
reviews ask for the page by name. This design turns the gap into a product plan.

## The framework: three layers, one owner each

- **Identity - "you are who you say you are."** Owned by the customer's IdP once SSO is
  configured. The new layer; today FlowRunner owns it via passwords.
- **Membership - "you belong in this workspace."** Owned by the Team roster, by invitation.
  Unchanged.
- **Reach - "what you can touch."** Owned by Permissions. Unchanged.

SSO is a **workspace authentication policy**, not a membership system: the IdP decides who gets
in the door; FlowRunner decides who belongs and what they can reach. The Team page's mental model
is untouched, and "no per-seat charges" stays true.

### Decisions taken (with the alternatives that were rejected)

1. **Anchor: per-workspace SSO.** Configured in Workspace Settings, applies to that workspace's
   team. Rejected: verified-email-domain routing (Slack/Notion pattern; no workspace fit today)
   and a new Organization layer (a restructuring, not a feature).
2. **Membership: invitation stays king.** The roster admits people; the IdP only authenticates
   them. Rejected: JIT admission (IdP as second membership authority) and an admin toggle for
   both (two admission models, double the support surface).
3. **Sign-in: SSO all the way.** Members of an enforced workspace never need a FlowRunner
   password. Rejected: step-up-only at the workspace door (every employee still holds a
   password - the thing IT adopts SSO to eliminate).
4. **Protocol: SAML 2.0 only in v1.** Covers every IdP the pricing page names; "any SAML 2.0
   IdP" is the support statement. OIDC is a fast-follow. LDAP is descoped to its own later
   effort (directory protocol, not federation; mostly self-hosted relevance).

## Admin setup journey

Workspace Settings gains a **Single Sign-On** section, available on the Business plan and up
(below Business the section shows the upgrade path). Setup is a two-sided exchange, presented
as one:

- **FlowRunner's side, given:** the SP details the IdP admin needs - ACS URL, Entity ID,
  metadata URL - displayed with copy buttons.
- **The customer's side, pasted:** the IdP metadata URL (or uploaded metadata XML), which
  auto-fills SSO URL, issuer, and signing certificate. Manual fields exist as fallback.
- **Matching rule, stated plainly in the UI:** the assertion's NameID is an email address, and
  it must match an invited roster member's email.
- **Test connection:** runs a real assertion in a popup with the admin's own IdP account and
  shows the parsed result (email, attributes) before anything is enforced.

Configuration states: **Not configured -> Configured (optional) -> Enforced.** Enforced is
unreachable without a passing test connection.

## Enforcement and the break-glass rule

"Require SSO for this workspace" is the enforcement toggle. On: every member entering the
workspace needs a fresh IdP assertion; password entry to this workspace stops working. Two
non-negotiable safety rules:

- **The Owner always retains FlowRunner-credential access** to the workspace - the one account
  that survives an IdP outage or a botched configuration. Stated in the UI next to the toggle.
- **Enforcement cannot be enabled without a passing test connection** - prevents the
  self-lockout case that fills every SSO support queue.

## Member journeys

- **First time:** accept the email invite -> sent straight to the company IdP -> account created
  or linked on the assertion. No password step.
- **Daily:** "Sign in with SSO" on the login page (email in, redirect out), or IdP-initiated -
  the FlowRunner tile in the IdP dashboard lands them in the workspace.
- **Mixed life:** a member who also belongs to non-SSO workspaces can hold a password for those;
  the enforced workspace's door always demands the IdP.
- **Deprovisioned at the IdP:** the next assertion fails; the next entry attempt shows a clear
  locked-out screen naming the workspace and pointing at their admin. The roster row remains
  until the admin removes it - membership is the admin's ledger. Flows are workspace-scoped, not
  personally owned, so nothing the person built stops running. *(Behavior assertion - product
  team to confirm.)*

## One account, many credentials

Raised in design review: what happens when an SSO-workspace member creates their own non-SSO
workspace? Answer: **no re-registration, ever.** One human stays one account; what varies is
which credentials the account holds.

- An account can hold several sign-in methods at once: an optional password, and one or more
  durable IdP links (bound at first assertion; a later account-email change does not break the
  binding).
- A password-less member already has an account-wide session via their IdP sign-in, so creating
  a workspace or accepting any invite works immediately.
- **Creating a workspace makes you its Owner, and the break-glass rule says an Owner holds
  FlowRunner credentials** - so workspace creation by a password-less user prompts them to set a
  password (verified by email) as part of the flow.
- Accepting an invite to someone else's non-SSO workspace triggers the same prompt, skippable,
  with the warning that skipping leaves this access riding on the employer's IdP.
- "Set a password" lives permanently in account settings; the ordinary reset-by-email flow works
  for any account. The unsolvable case - losing IdP access and the work email simultaneously -
  is why the prompt fires early rather than at departure time.

## Scope

**In v1:** SAML 2.0 SP-initiated and IdP-initiated sign-in; workspace SSO configuration UI with
test connection; enforcement with break-glass; password-less invite acceptance; login-page SSO
path; lockout screen; password-setup prompts for password-less users; plan gating at Business.

**Named IdP setup guides (Okta, Entra ID, Google Workspace, OneLogin) are docs work, not code.**

**Non-goals for v1:** OIDC (fast-follow), SCIM or any automated provisioning, JIT admission,
LDAP (separate later effort; pricing page's Enterprise LDAP line stays roadmap), an Organization
layer, consolidated billing, per-workspace session policies.

## Open questions for the product team (unanswered by design; carried in the epic)

1. Session lifetime of a workspace assertion, and re-auth cadence.
2. Does toggling enforcement on, or IdP-deprovisioning, kill *active* sessions or bite at next
   entry?
3. Assertion signing/encryption requirements (signed assertions mandatory? encrypted supported?).
4. One IdP serving several workspaces (same company, many teams) without duplicate configuration.
5. Audit logging of SSO configuration changes and of Owner break-glass sign-ins.
6. Confirm flows are workspace-scoped with no personally-owned runtime dependency (assumed in
   the deprovisioning journey).

## Docs follow-up (after the feature exists)

The original brief's page (`platform/single-sign-on.md`) gets written against the shipped
product through the standard loop (plan -> in-product verification -> gate -> Mark). Its
structure will fall out of this design: the three-layer framework, admin setup, member sign-in,
deprovisioning, plan gating - plus a boundary paragraph distinguishing SSO from OAuth
Connections (your IdP signing people into FlowRunner vs FlowRunner signing into other services).
