import type { ButtonHTMLAttributes } from "react";

import { cn } from "../../lib/utils";

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement>;

export function Button({ className, ...props }: ButtonProps) {
  return (
    <button
      className={cn("rounded-md bg-[#17231e] px-5 py-3 text-xs font-bold text-white transition hover:bg-[#2f4d3e]", className)}
      {...props}
    />
  );
}
