# Manual Test Cases

Application: https://www.saucedemo.com

| ID | Module | Title | Steps | Expected result | Priority | Automated |
|----|--------|-------|-------|-----------------|----------|-----------|
| TC01 | Login | Login with valid credentials | 1. Open site 2. Enter `standard_user` / `secret_sauce` 3. Click Login | Products page opens | High | Yes |
| TC02 | Login | Login with wrong password | Enter valid user and wrong password | Error: "Username and password do not match" | High | Yes |
| TC03 | Login | Login with empty username | Leave username blank, enter password | Error: "Username is required" | Medium | Yes |
| TC04 | Login | Login with empty password | Enter username, leave password blank | Error: "Password is required" | Medium | Yes |
| TC05 | Login | Locked out user | Login as `locked_out_user` | Error says the user is locked out | High | Yes |
| TC06 | Login | Access inventory without login | Open `/inventory.html` directly | Error shown, user stays on login page | High | Yes |
| TC07 | Login | Logout | Login, open menu, click Logout | Login page is shown | Medium | Yes |
| TC08 | Inventory | Product count | Login and view products | 6 products are listed | Medium | Yes |
| TC09 | Inventory | Sort price low to high | Select "Price (low to high)" | Prices ascending | Medium | Yes |
| TC10 | Inventory | Sort price high to low | Select "Price (high to low)" | Prices descending | Medium | Yes |
| TC11 | Inventory | Sort name Z to A | Select "Name (Z to A)" | Names in reverse alphabetical order | Low | Yes |
| TC12 | Cart | Add item to cart | Click Add to cart on one product | Cart badge shows 1 | High | Yes |
| TC13 | Cart | Remove item from cart | Add two items, remove one | Badge shows 1 | Medium | Yes |
| TC14 | Cart | Cart shows correct item | Add backpack, open cart | Cart lists Sauce Labs Backpack | High | Yes |
| TC15 | Checkout | Complete purchase | Add item, checkout, fill details, finish | "Thank you for your order!" | High | Yes |
| TC16 | Checkout | Missing first name | Leave first name blank on checkout | Error: "First Name is required" | Medium | Yes |
| TC17 | Checkout | Missing last name | Leave last name blank | Error: "Last Name is required" | Medium | Yes |
| TC18 | Checkout | Missing postal code | Leave postal code blank | Error: "Postal Code is required" | Medium | Yes |
