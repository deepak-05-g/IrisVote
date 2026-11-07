import { useState } from "react";
import type { FormEvent } from "react";

import { Button } from "../components/ui/button";
import { createRegistration, type RegistrationPayload } from "../lib/api";

const initialForm: RegistrationPayload = {
  synthetic_voter_id: "",
  full_name: "",
  date_of_birth: "",
  address: "",
  contact_number: "",
};

export default function Register() {
  const [form, setForm] = useState(initialForm);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  function updateField(field: keyof RegistrationPayload, value: string) {
    setForm((current) => ({ ...current, [field]: value }));
    setError("");
    setSuccess("");
  }

  function validate(): string {
    if (!form.full_name.trim() || !form.date_of_birth || !form.address.trim() || !form.synthetic_voter_id.trim()) {
      return "Complete all required fields before submitting.";
    }
    if (!/^IV-[A-Z0-9]{6}$/.test(form.synthetic_voter_id.trim())) {
      return "Synthetic voter ID must use the format IV-XXXXXX.";
    }
    const birthDate = new Date(`${form.date_of_birth}T00:00:00`);
    if (Number.isNaN(birthDate.getTime()) || birthDate >= new Date()) {
      return "Date of birth must be a valid date in the past.";
    }
    return "";
  }

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (isSubmitting) return;
    const validationError = validate();
    if (validationError) {
      setError(validationError);
      return;
    }
    setIsSubmitting(true);
    setError("");
    try {
      const registration = await createRegistration({
        ...form,
        synthetic_voter_id: form.synthetic_voter_id.trim(),
        full_name: form.full_name.trim(),
        address: form.address.trim(),
        contact_number: form.contact_number?.trim(),
      });
      setSuccess(`Registration ${registration.synthetic_voter_id} was submitted for review.`);
      setForm(initialForm);
    } catch (submissionError) {
      setError(submissionError instanceof Error ? submissionError.message : "Registration could not be completed.");
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <main className="registration-shell">
      <a className="back-link" href="/">← Back to IrisVote</a>
      <div className="registration-heading">
        <p className="eyebrow">Synthetic prototype registration</p>
        <h1>Register a voter identity for review.</h1>
        <p>Use fictional data only. This stage collects no iris images and does not connect identity to ballot choices.</p>
      </div>
      <form className="registration-form" onSubmit={submit} noValidate>
        <label>Full name<input value={form.full_name} onChange={(event) => updateField("full_name", event.target.value)} placeholder="Asha Prototype" required /></label>
        <label>Date of birth<input type="date" value={form.date_of_birth} onChange={(event) => updateField("date_of_birth", event.target.value)} required /></label>
        <label className="full-width">Address<textarea value={form.address} onChange={(event) => updateField("address", event.target.value)} placeholder="Synthetic testing address" required /></label>
        <label>Synthetic voter ID<input value={form.synthetic_voter_id} onChange={(event) => updateField("synthetic_voter_id", event.target.value.toUpperCase())} placeholder="IV-ABC123" pattern="IV-[A-Z0-9]{6}" required /></label>
        <label>Contact number <span>(optional)</span><input value={form.contact_number} onChange={(event) => updateField("contact_number", event.target.value)} placeholder="+91 90000 00000" /></label>
        {error && <p className="form-message error" role="alert">{error}</p>}
        {success && <p className="form-message success" role="status">{success}</p>}
        <div className="form-actions"><Button type="submit" disabled={isSubmitting}>{isSubmitting ? "Submitting…" : "Submit for review"}</Button><small>Required fields are marked by the browser.</small></div>
      </form>
    </main>
  );
}
