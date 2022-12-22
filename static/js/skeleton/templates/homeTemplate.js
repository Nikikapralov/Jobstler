import { html } from "../node_modules/lit-html/lit-html.js"

export function homeTemplate(ctx){
    return html`
 <section class="Home">
            <h1>Jobstler</h1>
            <div class="img_container">
            <img class="left" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXtpxyUNqvDwB0nFguGKdmQJksEKOb4V8g4PkTalVE&s" alt="">
                <img class="right" src="https://images.unsplash.com/photo-1551434678-e076c223a692?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fG9mZmljZSUyMHdvcmt8ZW58MHx8MHx8&w=1000&q=80" alt=""></div>
                <p>
                    At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.</p>
                    <img class="middle" src="https://img.freepik.com/free-photo/pleased-woman-with-light-brown-skin-posing-with-crossed-arms-smiling-while-people-her-working-indoor-portrait-tired-students-with-laptop-african-curly-girl_197531-3760.jpg?w=2000">
                    <h2>Publish a job opportunity and find quality workers now!</h2>
                    <a href="/register">Register</a>

        </section>
    `
}