import { html } from "../node_modules/lit-html/lit-html.js"
import { onSubmit } from "../eventListeners/form/submit.js"
import { register } from "../services/auth.js"
import { noEmptyFields, passwordsMatch } from "../validators/formValidators.js"

export function registerTemplate(ctx){
    let validators = []
    return html`
        <section class="Register">
            <form @submit=${onSubmit(register, validators, ctx, "/")}>
                <h3>Register</h3>
                <input type="text" placeholder="Your email" name="email">
                <input type="password" placeholder="Your password" name="password">
                <input type="password" placeholder="Confirm your password" name="conf-password">
                <button type="submit">Register</button>
            </form>
        </section>
    `
}