import page from "../node_modules/page/page.mjs";
import { renderNavbar } from "../middlewares/navbarRenderer.js";
import { attachRender } from "../middlewares/renderAttacher.js";
import {homeHandler} from "../handlers/homeHandler.js";
import {loginHandler} from "../handlers/loginHandler.js";
import {registerHandler} from "../handlers/registerHandler.js";
import {logoutHandler} from "../handlers/logoutHandler.js";

page(renderNavbar)
page(attachRender)

page("/", homeHandler)
page("/login", loginHandler)
page("/register", registerHandler)

page.start()