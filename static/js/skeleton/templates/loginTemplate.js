import { html } from "../node_modules/lit-html/lit-html.js"
import { onSubmit } from "../eventListeners/form/submit.js"
import { login } from "../services/auth.js"
import { noEmptyFields } from "../validators/formValidators.js"


export function loginTemplate(ctx){
    let validators = []
    return html`
        <section class="Log in">
    <form @submit=${onSubmit(login, validators, ctx, "/")}>
        <h3>Log in</h3>
        <input type="text" placeholder="Your email" name="email">
            <input type="password" placeholder="Your password" name="password">
                <button type="submit">Log in</button>
    </form>
</section>
    `
}