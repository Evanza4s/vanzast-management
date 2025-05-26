import NewsSection from "@/section/NewsSection";
import HomeClient from "./(home)/page";
import AboutSection from "@/section/AboutSection";
import CharacterSection from "@/section/CharacterSection";
import ContactSection from "@/section/ContactSection";
import FAQSection from "@/section/FAQSection";

export default function Home() {
  return (
    <div>
      <HomeClient />
      <NewsSection />
      <AboutSection />
      <CharacterSection />
      <ContactSection />
      <FAQSection />
    </div>
  );
}
