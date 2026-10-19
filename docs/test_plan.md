# Test Plan: SauceDemo & JSONPlaceholder

## 1. Objective
Verify the core user flows of the SauceDemo web store (login, product listing, cart, checkout) and the basic CRUD behaviour of the JSONPlaceholder REST API.

## 2. Scope
**In scope**
- Login: valid, invalid, locked-out user, direct URL access without login, logout
- Inventory: product count, sorting (name, price)
- Cart: add, remove, badge count, cart contents
- Checkout: complete order, form field validation
- API: GET, POST, PUT, DELETE on `/posts`, filtering, 404 handling

**Out of scope**
- Performance, security and load testing
- Cross-browser testing (Chromium only)
- Mobile devices

## 3. Test approach
| Type | How |
|------|-----|
| Manual | Test cases written in `docs/test_cases.md` |
| UI automation | Playwright + pytest using the Page Object Model |
| API automation | pytest + requests |
| Reporting | pytest-html report, screenshots on failure |
| CI | GitHub Actions on every push |

## 4. Test environment
- Application: https://www.saucedemo.com (public demo site)
- API: https://jsonplaceholder.typicode.com (fake online REST API)
- Browser: Chromium (Playwright)
- Language: Python 3.10+

## 5. Test data
Public demo credentials: `standard_user`, `locked_out_user` with password `secret_sauce`.

## 6. Entry and exit criteria
- Entry: test site reachable, dependencies installed
- Exit: all smoke tests pass, no open critical defects

## 7. Risks
- Public demo sites can be slow or down, which causes flaky failures.
- JSONPlaceholder does not really save changes (POST, PUT and DELETE only simulate success).
