import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host:'0.0.0.0' // listen on all network interfaces
  },
 base: "/skylight/",
  plugins: [vue()],
  resolve: {
    alias: {
      "@/": `${__dirname}/src/`,
    },
  },

}
);
