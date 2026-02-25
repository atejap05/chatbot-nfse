import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Assistente NFS-e",
  description: "Chatbot especializado em Nota Fiscal de Serviços Eletrônica",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body className="antialiased">{children}</body>
    </html>
  );
}
