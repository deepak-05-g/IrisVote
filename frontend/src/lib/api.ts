const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export type RegistrationPayload = {
  synthetic_voter_id: string;
  full_name: string;
  date_of_birth: string;
  address: string;
  contact_number?: string;
};

export type RegistrationResponse = RegistrationPayload & {
  id: number;
  status: string;
  created_at: string;
};

export async function createRegistration(
  payload: RegistrationPayload,
): Promise<RegistrationResponse> {
  let response: Response;
  try {
    response = await fetch(`${API_BASE_URL}/api/v1/registrations`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
  } catch {
    throw new Error("The registration service is unavailable. Please try again.");
  }

  const body = await response.json().catch(() => null);
  if (!response.ok) {
    throw new Error(body?.detail || "Registration could not be completed.");
  }
  return body as RegistrationResponse;
}
