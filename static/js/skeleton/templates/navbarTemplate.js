import { html } from "../node_modules/lit-html/lit-html.js"
import { onClick } from "../eventListeners/button/click.js"
import { logout} from "../services/auth.js"

export function navbarTemplateNotLogged(ctx){
    return html`
     <nav class="header_non_authenticated">
            <ul>
                <li>
                    <a class="home" href="/">Home</a>
                </li>
                <li>
                    <a href="/register" class="register">Register</a>
                </li>
                <li>
                    <a href="/login" class="log-in">Log in</a>
                </li>
            </ul>
        </nav>
    `
}

export function navbarTemplateLogged(ctx){
    return html`
         <nav class="header_authenticated">
            <ul>
                <li>
                    <a href="/">Home</a>
                </li>
                <li>
                    <a href="/my_profile">My Profile</a>
                </li>
                <li>
                    <a href="/my_advertisments">My Advertisements</a>
                </li>
                <li>
                    <a href="/advertisements" class="advertisements">Advertisements</a>
                </li>
                <li>
                    <a href="/advertisements/create">Create advertisement</a>
                </li>
                <li>
                    <a <a @submit=${onSubmit(logout, [], ctx, "/")} href="/logout" class="log_out">Log out</a>
                </li>
            </ul>
        </nav>
    `
}

export function navbarTemplateLoggedAdmin(ctx){
    return html`
            <nav class="header_admin">
            <ul>
                <li>
                    <a href="/">Home</a>
                </li>
                <li>
                    <a href="/user_profiles" class="user_profiles">User profiles</a>
                </li>
                <li>
                    <a @submit=${onSubmit(logout, [], ctx, "/")} href="/logout" class="log_out">Log out</a>
                </li>
            </ul>
        </nav>
    `
}
