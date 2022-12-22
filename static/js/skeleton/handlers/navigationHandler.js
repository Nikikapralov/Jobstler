import { navbarTemplateLogged, navbarTemplateNotLogged, navbarTemplateLoggedAdmin } from "../templates/navbarTemplate.js";
import { getUser } from "../services/auth.js"

export function navigationHandler(ctx){
    let user = getUser()
    if (user == undefined){
        return navbarTemplateNotLogged(ctx)
    }
    if (user["Authorization"] && user["is_superuser"]){
        return navbarTemplateLoggedAdmin(ctx)
    }
    else if (user["Authorization"]){
        return navbarTemplateLogged(ctx)
    }
}