import { render } from "lit-html"
import { navigationHandler } from "../handlers/navigationHandler.js"


let headerElement = document.getElementsByTagName("header")[0]

export function renderNavbar(ctx, next){
    render(navigationHandler(ctx), headerElement)
    next()
}