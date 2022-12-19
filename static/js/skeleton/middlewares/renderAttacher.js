import { render } from "lit-html";

let mainContent = document.getElementsByTagName("main")[0]

function renderWrapper(template){
    render(template, mainContent)
}

export function attachRender(ctx, next){
    ctx.render = renderWrapper
    next()
}