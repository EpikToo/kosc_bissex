import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BissexRangeComponent } from './bissex-range.component';

describe('BissexRangeComponent', () => {
  let component: BissexRangeComponent;
  let fixture: ComponentFixture<BissexRangeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BissexRangeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BissexRangeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
