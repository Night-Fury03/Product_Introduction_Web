/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html, ./src/**/*.{vue,js,ts}"],
  theme: {
    extend: {
      colors: {
        primary: "#003366", // Xanh đậm - màu chủ đạo
        secondary: "#FF6600", // Cam - điểm nhấn
        background: "#F5F5F5", // Xám nhạt - nền
        text: "#2E2E2E", // Xám đậm - chữ
        border: "#A0A0A0", // Bạc - viền
        warning: "#CC0000", // Đỏ cảnh báo
      },
    },
    fontFamily: {
      Montserrat: "Montserrat, san-serif"
    },
    container: {
      center: true,
      padding: {
        DEFAULT: "2rem", // Giảm padding mặc định
        sm: "2.5rem",
        md: "3rem",
        lg: "4rem", // Giữ nguyên padding lớn khi viewport rộng
      }
    },
  },
  corePlugins: {
    preflight: true, // Đảm bảo Preflight đang bật
  },
  plugins: [],
}

