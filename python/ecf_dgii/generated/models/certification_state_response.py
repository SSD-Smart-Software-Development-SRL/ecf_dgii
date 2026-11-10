from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.certification_step_type_1 import CertificationStepType1
from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificationStateResponse")


@_attrs_define
class CertificationStateResponse:
    """
    Attributes:
        state (str | Unset): One of CertificationStates.
        source (None | str | Unset): One of CertificationStateSources; null while not started.
        step (CertificationStepType1 | None | Unset):
        step_number (int | None | str | Unset): Visible step number, 1 to int CertificationStateResponse.TotalSteps.
        total_steps (int | str | Unset):
        responsible (None | str | Unset): One of CertificationResponsibles while in progress.
        stalled (bool | Unset): In progress without any activity for int CertificationStateCalculator.StalledAfterDays
            days.
        last_activity_on (datetime.datetime | None | Unset):
        certified_on (datetime.date | None | Unset): DGII authorisation date, when known (DGII listing or declared by
            the customer).
        changed_on (datetime.datetime | None | Unset): When the stored state last changed.
        signature_review_pending (bool | Unset): A step was signed outside the platform and the signature could not be
            verified (CERT-04).
    """

    state: str | Unset = UNSET
    source: None | str | Unset = UNSET
    step: CertificationStepType1 | None | Unset = UNSET
    step_number: int | None | str | Unset = UNSET
    total_steps: int | str | Unset = UNSET
    responsible: None | str | Unset = UNSET
    stalled: bool | Unset = UNSET
    last_activity_on: datetime.datetime | None | Unset = UNSET
    certified_on: datetime.date | None | Unset = UNSET
    changed_on: datetime.datetime | None | Unset = UNSET
    signature_review_pending: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        step: None | str | Unset
        if isinstance(self.step, Unset):
            step = UNSET
        elif isinstance(self.step, CertificationStepType1):
            step = self.step.value
        else:
            step = self.step

        step_number: int | None | str | Unset
        if isinstance(self.step_number, Unset):
            step_number = UNSET
        else:
            step_number = self.step_number

        total_steps: int | str | Unset
        if isinstance(self.total_steps, Unset):
            total_steps = UNSET
        else:
            total_steps = self.total_steps

        responsible: None | str | Unset
        if isinstance(self.responsible, Unset):
            responsible = UNSET
        else:
            responsible = self.responsible

        stalled = self.stalled

        last_activity_on: None | str | Unset
        if isinstance(self.last_activity_on, Unset):
            last_activity_on = UNSET
        elif isinstance(self.last_activity_on, datetime.datetime):
            last_activity_on = self.last_activity_on.isoformat()
        else:
            last_activity_on = self.last_activity_on

        certified_on: None | str | Unset
        if isinstance(self.certified_on, Unset):
            certified_on = UNSET
        elif isinstance(self.certified_on, datetime.date):
            certified_on = self.certified_on.isoformat()
        else:
            certified_on = self.certified_on

        changed_on: None | str | Unset
        if isinstance(self.changed_on, Unset):
            changed_on = UNSET
        elif isinstance(self.changed_on, datetime.datetime):
            changed_on = self.changed_on.isoformat()
        else:
            changed_on = self.changed_on

        signature_review_pending = self.signature_review_pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if source is not UNSET:
            field_dict["source"] = source
        if step is not UNSET:
            field_dict["step"] = step
        if step_number is not UNSET:
            field_dict["stepNumber"] = step_number
        if total_steps is not UNSET:
            field_dict["totalSteps"] = total_steps
        if responsible is not UNSET:
            field_dict["responsible"] = responsible
        if stalled is not UNSET:
            field_dict["stalled"] = stalled
        if last_activity_on is not UNSET:
            field_dict["lastActivityOn"] = last_activity_on
        if certified_on is not UNSET:
            field_dict["certifiedOn"] = certified_on
        if changed_on is not UNSET:
            field_dict["changedOn"] = changed_on
        if signature_review_pending is not UNSET:
            field_dict["signatureReviewPending"] = signature_review_pending

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = d.pop("state", UNSET)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_step(data: object) -> CertificationStepType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_certification_step_type_1 = CertificationStepType1(data)

                return componentsschemas_certification_step_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CertificationStepType1 | None | Unset, data)

        step = _parse_step(d.pop("step", UNSET))

        def _parse_step_number(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        step_number = _parse_step_number(d.pop("stepNumber", UNSET))

        def _parse_total_steps(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        total_steps = _parse_total_steps(d.pop("totalSteps", UNSET))

        def _parse_responsible(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        responsible = _parse_responsible(d.pop("responsible", UNSET))

        stalled = d.pop("stalled", UNSET)

        def _parse_last_activity_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_on_type_1 = datetime.datetime.fromisoformat(data)

                return last_activity_on_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity_on = _parse_last_activity_on(d.pop("lastActivityOn", UNSET))

        def _parse_certified_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                certified_on_type_1 = datetime.date.fromisoformat(data)

                return certified_on_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        certified_on = _parse_certified_on(d.pop("certifiedOn", UNSET))

        def _parse_changed_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                changed_on_type_1 = datetime.datetime.fromisoformat(data)

                return changed_on_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        changed_on = _parse_changed_on(d.pop("changedOn", UNSET))

        signature_review_pending = d.pop("signatureReviewPending", UNSET)

        certification_state_response = cls(
            state=state,
            source=source,
            step=step,
            step_number=step_number,
            total_steps=total_steps,
            responsible=responsible,
            stalled=stalled,
            last_activity_on=last_activity_on,
            certified_on=certified_on,
            changed_on=changed_on,
            signature_review_pending=signature_review_pending,
        )

        certification_state_response.additional_properties = d
        return certification_state_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
