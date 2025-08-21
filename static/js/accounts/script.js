// Efeito de entrada animado nos botões
document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".btn");

    buttons.forEach((btn, index) => {
        setTimeout(() => {
            btn.style.opacity = "1";
            btn.style.transform = "translateY(0)";
        }, index * 300);
    });

    // Efeito ao clicar nos botões
    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            btn.classList.add("clicked");
            setTimeout(() => {
                btn.classList.remove("clicked");
            }, 500);
        });
    });
});