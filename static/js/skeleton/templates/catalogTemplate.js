import { html } from "lit-html"
import { singleEntry } from "./singleEntryTemplate.js"

export function catalogTemplate(ctx, entries){
    if (Object.keys(entries).length == 0){
        return html`
         <h2>No products yet.</h2>
        `
    }

    return html` <h2>Products</h2>
    <section id="dashboard">
        ${entries.map( (x) => singleEntry(x))}
    </section>
    `
}