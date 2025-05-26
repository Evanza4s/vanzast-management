"use client";
import React from "react";
import { NavbarItem } from "@/constant/navbar";
import Link from "next/link";
import { cn } from "@/lib/utils";
import useScroll from "@/hooks/use-scroll";
import { useSelectedLayoutSegment } from "next/navigation";
import Image from "next/image";
import Logo from "@/assets/images/Logo.png"

const HomeNavigation = () => {
  const scrolled = useScroll(5);
  const selectedLayout = useSelectedLayoutSegment();

  return (
    <header
      className={cn(
        `sticky top-0 inset-x-0 w-full transition-all z-50 bg-transparent hidden md:block`,
        {
          "border-b border-gray-200 bg-red-500/75 text-black backdrop-blur-lg": scrolled,
          "border-b border-gray-200 bg-white": selectedLayout,
        }
      )}
    >
      <nav className="@container">
        <div className="flex justify-between items-center py-4 px-12">
          <div className="flex flex-row items-center gap-5">
            <Image src={Logo} alt="Logo" className="h-10 w-auto" />
            <h1 className="text-3xl font-semibold">LOGO</h1>
          </div>

          <ul className="flex justify-center items-center gap-8">
            {NavbarItem.map((item, idx) => (
              <li key={idx}>
                <Link href={item.path}>
                  <h1 className="lg:text-xl text-base">{item.title}</h1>
                </Link>
              </li>
            ))}
          </ul>

          <div className="gap-10 items-baseline hidden lg:flex">
            <button>Get Started</button>
            <button>Login</button>
          </div>
        </div>
        
      </nav>
    </header>
  );
};

export default HomeNavigation;
