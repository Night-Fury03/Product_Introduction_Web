/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html, ./src/**/*.{vue,js,ts}"],
  theme: {
    extend: {},
    fontFamily: {
      Montserrat: "Montserrat, san-serif"
    },
    container: {
      center: true,
      padding: "2rem",
    }
  },
  plugins: [],
}

