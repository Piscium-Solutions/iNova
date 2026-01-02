# Final Test App: Frappe Quickstart

This repository contains a lightweight Frappe app scaffold (`my_naito_app`) you can use to experiment with building a simple app. The steps below walk through setting up a local bench, installing the app on a fresh site, and adding a very small feature so you have a working starting point.

## 1. Prepare a bench and site
1. Install [bench](https://frappeframework.com/docs/user/en/bench/resources/bench-cli) in your environment if you have not already.
2. Create a bench and site (replace the domain with one that suits your setup):

   ```bash
   bench init --frappe-branch version-15 frappe-bench
   cd frappe-bench
   bench new-site demo.localhost
   ```

3. Add this app to the bench. If you already have the code locally, point bench to it; otherwise clone it first:

   ```bash
   bench get-app my_naito_app /workspace/iNova
   bench --site demo.localhost install-app my_naito_app
   bench start
   ```

At this point you can log in at `http://localhost:8000` with the site credentials you set during `bench new-site`.

## 2. Create a simple DocType
You can build a minimal feature by defining a `Simple Note` DocType with two fields.

1. From the Desk, open **Developer > DocType** and click **New**.
2. Fill in the form:
   - **DocType Name:** `Simple Note`
   - **Module:** `Final Test App`
   - **Custom?** Leave unchecked (the definition will live in this app).
3. Add these fields:
   - **Title** – **Field Type:** *Data* (mark as required)
   - **Content** – **Field Type:** *Small Text*
4. Save and **Publish** the DocType so it creates the database table.

Once saved you can create `Simple Note` records from the Desk or via the API.

## 3. Add a tiny API endpoint
The app now includes a whitelisted helper (`quick_hello`) that you can call from the browser or a client. It lives in `final_test_app/api.py` and simply echoes a greeting.

- Test it from the browser (guest access is allowed):

  ```bash
  curl "http://demo.localhost:8000/api/method/final_test_app.api.quick_hello?name=Sam"
  ```

  Response:

  ```json
  {"message": "Hello, Sam! Welcome to your first Frappe app."}
  ```

- Use it inside server-side Python to reuse the greeting logic:

  ```python
  from final_test_app.api import quick_hello

  print(quick_hello(name="Sam")['message'])
  # -> "Hello, Sam! Welcome to your first Frappe app."
  ```

## 4. Next steps
- Add form validation or workflows in `simple_note.py` (created alongside the DocType).
- Expose additional whitelisted methods to create or list notes using `frappe.get_doc` and `frappe.get_all`.
- Add a module card for your feature in `config/desktop.py` so it appears on the Desk home page.

These patterns should give you a functional starting point for experimenting with the Frappe framework.
