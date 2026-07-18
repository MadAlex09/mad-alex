document.addEventListener("DOMContentLoaded", function () {

    const openProjectButton =
        document.getElementById("open-project");

    const projectModal =
        document.getElementById("project-modal");

    const closeModalButton =
        document.getElementById("close-modal");


    openProjectButton.addEventListener("click", function (event) {

        event.preventDefault();

        projectModal.style.display = "flex";

    });


    closeModalButton.addEventListener("click", function () {

        projectModal.style.display = "none";

    });


    projectModal.addEventListener("click", function (event) {

        if (event.target === projectModal) {

            projectModal.style.display = "none";

        }

    });

});

const contactForm =
    document.getElementById("contact-form");


contactForm.addEventListener(
    "submit",
    function(event) {

        event.preventDefault();


        const name =
            document.getElementById("client-name").value;


        const contact =
            document.getElementById("client-contact").value;


        const message =
            document.getElementById("client-message").value;


        alert(
            "Заявка отправлена!\n\n" +
            "Спасибо, " + name + "!"
        );


        contactForm.reset();

    }
);