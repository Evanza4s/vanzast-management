import { HtmlHTMLAttributes } from "react";
import { twMerge } from "tailwind-merge";

export const BodyContainer = (props: HtmlHTMLAttributes<HTMLDivElement>) => {
    const {className, ...otherProps} = props
    return <div className={twMerge('@container py-12 md:py-18 lg:py-24 overflow-hidden ', className)} {...otherProps} />;
}